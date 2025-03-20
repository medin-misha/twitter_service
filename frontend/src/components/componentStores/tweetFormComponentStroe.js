import { defineStore, storeToRefs } from "pinia";
import { useAPIStore } from "@/stores/useAPIStore";
import { useLoginStore } from "@/stores/useLoginStore";

export const useTweetFormComponentStore = defineStore("tweetFormComponent", {
  state: () => ({
    tweet_data: "",
    tweet_media_id: NaN,
    api_key: "",
    apiStore: useAPIStore(),
    key: storeToRefs(useLoginStore()).key,
    file: null,
  }),
  getters: {
    fileUrl: (state) => (state.file ? URL.createObjectURL(state.file) : ""),
  },
  actions: {
    async createTweet() {
      let tweet_data_id = null;
      if (this.file) {
        tweet_data_id = await this.apiStore.saveMedia(this.file, this.key);
      }
      const response = await this.apiStore.createTweet(
        {
          tweet_data: this.tweet_data,
          tweet_media_ids: tweet_data_id.result ? [tweet_data_id.media_id] : [],
        },
        this.key
      );
      return response.result ? true : false;
    },
    saveFile(event) {
      this.file = event.target.files[0];
    },
  },
});
