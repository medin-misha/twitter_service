import { defineStore } from "pinia";


export const useLoginComponentStore = defineStore("loginComponent", {
    state: () => ({
        isError: false,
        text: "Аутентифицируйтесь..",
        class_: "login-message",
        defaultClass: "login-message",
        errorClass: "error-login-message",
        successClass: "success-login-message",
        loginText: "Аутентифицируйтесь..",
        loginSuccessText: "Вы аутентифицированны!",
        loginErrorText: "Такой пользователь не найден.",
        successColor: "#8f94fb",
        errorColor: "#dd1818",
        defaultColor: "#2196f3"
    }),
    actions: {
        successLogin() {
            this.text = this.loginSuccessText;
            this.class_ = this.successClass;
            setTimeout(() => {
                this.class_ = this.defaultClass;
            }, 2000)
        },
        errorLogin() {
            this.text = this.loginErrorText;
            this.class_ = this.errorClass;
            setTimeout(() => {
                this.text = this.loginErrorText;
                this.class_ = this.defaultClass
            }, 1000)
        }
    }
})

