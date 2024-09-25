import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'
import VueSetupExtension from 'vite-plugin-vue-setup-extend'
import mkcert from 'vite-plugin-mkcert'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(),
    VueDevTools(),
    VueSetupExtension(),
    //mkcert()
  ],
  server: {
    port:10000,
    host:true,
  }
})
