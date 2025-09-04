import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images: {
    domains: ['domineia.com'], // ✅ Adiciona o domínio permitido da imagem URL
  },
};

export default nextConfig;
