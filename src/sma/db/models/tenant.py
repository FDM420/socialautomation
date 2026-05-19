"""Tenant model — the root of multi-tenancy.

In Mode A (single_tenant) there's exactly one row, id=1.
In Mode B (multi_tenant) one row per subscriber.

Every other domain table has a `tenant_id` FK pointing here.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sma.db.base import Base, TimestampMixin

if TYPE_CHECKING:
    from sma.db.models.user import User


class SubscriptionStatus(str, Enum):
    NONE = "none"            # Mode A — no billing
    TRIALING = "trialing"    # Mode B — in 7-day trial
    ACTIVE = "active"        # Mode B — paid + current
    PAST_DUE = "past_due"    # Mode B — payment failed
    CANCELLED = "cancelled"  # Mode B — cancelled


class Tenant(Base, TimestampMixin):
    """One tenant = one customer's isolated workspace."""

    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    subscription_status: Mapped[str] = mapped_column(
        String(32), nullable=False, default=SubscriptionStatus.NONE.value
    )
    trial_ends_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Stripe linkage (Mode B only — null in Mode A)
    stripe_customer_id: Mapped[str | None] = mapped_column(String(64), nullable=True, unique=True)
    stripe_subscription_id: Mapped[str | None] = mapped_column(
        String(64), nullable=True, unique=True
    )

    # Relationships
    users: Mapped[list["User"]] = relationship(
        back_populates="tenant", cascade="all, delete-orphan"
    )
