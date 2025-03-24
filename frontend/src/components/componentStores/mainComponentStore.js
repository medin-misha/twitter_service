import { defineStore } from "pinia";


export const useMainComponentStore = defineStore("mainStore", {
    state: () => ({
        tweetsComponents: true,
    }),
    actions: {
        hideAndShowTweets(key) {
            this.tweetsComponents = key;
        }
      },
})