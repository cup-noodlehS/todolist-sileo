import { createRouter, createWebHistory } from "vue-router";
import TodoIndex from "./views/todoIndex.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/todo",
      component: TodoIndex,
    },
  ],
});

export default router;
