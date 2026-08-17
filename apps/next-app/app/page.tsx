import Image from "next/image";
import Link from "next/link";
import Like from "./_components/Like";
import Counter from "./_components/Counter";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <div className="flex gap-6">
        <Link href="/blog/1" prefetch>
          Blog1
        </Link>
        <Link href="/blog/2">Blog2</Link>
      </div>
      <Like />
      <Counter />
    </div>
  );
}
