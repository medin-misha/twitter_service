import { defineStore } from "pinia"


export const useLoginStore = defineStore("userData", {
    state: () => ({ id: 0, key: "noAuth", userName: null, myLikes: []}),
    getters: {},
    actions: {},
})
