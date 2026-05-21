import Link from "next/link";

export default function PublicLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen flex-col bg-white">
      <header className="border-b border-slate-200">
        <div className="mx-auto flex h-16 max-w-5xl items-center justify-between px-6">
          <Link href="/" className="text-base font-semibold text-slate-900">
            Summit Automates
          </Link>
          <nav className="flex items-center gap-6 text-sm">
            <Link href="/login" className="text-slate-600 hover:text-slate-900">
              Sign in
            </Link>
          </nav>
        </div>
      </header>
      <main className="flex-1">{children}</main>
      <footer className="border-t border-slate-200 py-8 text-sm text-slate-500">
        <div className="mx-auto flex max-w-5xl flex-col items-center justify-between gap-3 px-6 sm:flex-row">
          <span>© {new Date().getFullYear()} Summit Automates. All rights reserved.</span>
          <div className="flex gap-5">
            <Link href="/terms" className="hover:text-slate-900">
              Terms
            </Link>
            <Link href="/privacy" className="hover:text-slate-900">
              Privacy
            </Link>
            <Link href="/data-deletion" className="hover:text-slate-900">
              Data deletion
            </Link>
            <a
              href="mailto:admin@summitautomates.com"
              className="hover:text-slate-900"
            >
              Contact
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
