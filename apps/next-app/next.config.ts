import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // cacheComponents: true,
  // partialPrefetching: true,
  images: {
    remotePatterns: [
    {
      protocol: "https",
      hostname: "web-cdn.gachifans.com",
    },
    ],
  },
};

export default nextConfig;


