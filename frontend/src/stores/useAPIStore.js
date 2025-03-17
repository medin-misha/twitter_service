import { defineStore } from "pinia";
import axios from "axios";

export const useAPIStore = defineStore("api", {
  state: () => ({
    url: "http://127.0.0.1:8000/",
  }),
  actions: {
    async me(key) {
      try {
        const response = await axios.get(this.url + "api/users/me", {
          headers: { "api-key": key, "Content-Type": "application/json" },
        });
        return response.data;
      } catch (error) {
        console.error("Ошибка при получении данных пользователя:", error);
        return null;
      }

    },
    async createTweet(data, key) {
      const response = await axios.post(this.url + "api/tweets", data, {
        headers: {
          "Content-Type": "application/json",
          "api-key": key,
        },
      });
      return response.data;
    },
  },
});
