import Image from "next/image";
import Link from "next/link";
import Like from "./_components/Like";
import Counter from "./_components/Counter";
import VirtualList from "./_components/VirtualList";

export default function Home() {
  return (
    <div className="">
      {/* <div className="flex gap-6">
        <Link href="/blog/1" prefetch>
          Blog1
        </Link>
        <Link href="/blog/2">Blog2</Link>
      </div>
      <Like />
      <Counter /> */}
      <VirtualList />
    </div>
  );
}
