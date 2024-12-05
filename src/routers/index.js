import { createMemoryHistory, createRouter } from 'vue-router'
import HomeView from '@/pages/home.vue';
import AboutView from '@/pages/about.vue';
import ServicesView from '@/pages/services.vue';
import PortfolioView from '@/pages/portfolio.vue';
import Client from '@/pages/client.vue'
const routes = [
  {path: '/', component: HomeView },
  {path: '/about',meta: { title: "Sobre Nós" }, component : AboutView},
  {path: '/services',meta: { title: "o que Fazemos?" }, component : ServicesView},
  {path: '/portfolio',meta: { title: "Casos de Sucesso!" }, component : PortfolioView},
  {path: '/clients',meta: { title: "Encontre seus Arquivos" }, component : Client}
]
const router = createRouter({
  history: createMemoryHistory(),
  routes,
})
router.beforeEach((to, from, next) => {
  const defaultTitle = "N9 Agência Digital";
  document.title = to.meta.title || defaultTitle;
  next();
});
export default router