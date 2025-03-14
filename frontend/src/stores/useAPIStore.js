import { defineStore } from "pinia";
import axios from "axios";

export const userAPIStore = defineStore("api", {
  state: () => ({
    url: "http://127.0.0.1:8000/",
  }),
  actions: {
    async me(key) {
      const response = await axios.get(this.url + "api/users/me", {
        headers: { "api-key": key, "Content-Type": "application/json" },
      });
      return response.data;
    },
  },
});
