import Link from "next/link";

export default function Home() {
  return (
    <nav>
      <Link href="/blog/1" prefetch>
        Blog1
      </Link>
      <Link href="/blog/2">Blog2</Link>
    </nav>
  );
}
