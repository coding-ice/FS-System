import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <div className="flex gap-6">
        <Link href="/blog/1">Blog1</Link>
        <Link href="/blog/2">Blog2</Link>
      </div>
      <Image
        width={300}
        height={1000}
        src="https://web-cdn.gachifans.com/res/production/Spine/shiraxxshiraxx/Default/Home/BG.png"
        alt="bg"
        // unoptimized
        // preload
        // fetchPriority="high"
      />
    </div>
  );
}
