import "../node_modules/bootstrap/dist/css/bootstrap.css";
import "../node_modules/bootstrap/dist/js/bootstrap.js";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./routes";
import axios from "axios";
import sileo from "sileo";

sileo.defaults.baseUrl = "http://127.0.0.1:8000";

// axios.defaults.baseURL = import.meta.env.BASE_URL;

const app = createApp(App);

app.use(router);

app.mount("#app");
