<script setup>
import { useLoginStore } from '@/stores/useLoginStore';
import { storeToRefs } from 'pinia';

const refStore = storeToRefs(useLoginStore())
</script>

<template>
    <section class="create-comment-section">
        <form class="flex create-comment-form">
            <div class="flex">
                <svg xmlns="http://www.w3.org/2000/svg" class="svg-icon"
                    style="width: 3em; height: 3em;vertical-align: middle;fill: currentColor;overflow: hidden;"
                    viewBox="0 0 1024 1024" version="1.1">
                    <path
                        d="M843.282963 870.115556c-8.438519-140.515556-104.296296-257.422222-233.908148-297.14963C687.881481 536.272593 742.4 456.533333 742.4 364.088889c0-127.241481-103.158519-230.4-230.4-230.4S281.6 236.847407 281.6 364.088889c0 92.444444 54.518519 172.183704 133.12 208.877037-129.611852 39.727407-225.46963 156.634074-233.908148 297.14963-0.663704 10.903704 7.964444 20.195556 18.962963 20.195556l0 0c9.955556 0 18.299259-7.774815 18.962963-17.73037C227.745185 718.506667 355.65037 596.385185 512 596.385185s284.254815 122.121481 293.357037 276.195556c0.568889 9.955556 8.912593 17.73037 18.962963 17.73037C835.318519 890.311111 843.946667 881.019259 843.282963 870.115556zM319.525926 364.088889c0-106.287407 86.186667-192.474074 192.474074-192.474074s192.474074 86.186667 192.474074 192.474074c0 106.287407-86.186667 192.474074-192.474074 192.474074S319.525926 470.376296 319.525926 364.088889z" />
                </svg>
                <textarea placeholder="Ну шо ты?" name="create-comment-textarea" class="create-comment-textarea"
                    cols="73" rows="5"></textarea>
                <label for="input-image">
                    <svg class="input-file-svg" xmlns="http://www.w3.org/2000/svg" height="24px"
                        viewBox="0 -960 960 960" width="24px" fill="#e3e3e3">
                        <path
                            d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm40-80h480L570-480 450-320l-90-120-120 160Zm-40 80v-560 560Z" />
                    </svg>
                </label>
                <input type="file" id="input-image" class="input-image">
            </div>
            <button class="create-comment-button" type="button">отправить</button>
        </form>
    </section>
</template>

<style scoped>
.create-comment-section {
    padding-top: 1em;
}

.create-comment-textarea {
    all: unset;
}

.create-comment-textarea {
    border: none;
    background-color: #15202b;
    padding: 10px;
    max-width: 100%;
    line-height: 1.5;
    border-radius: 5px;
    border: 0;
    background: #15202b;
}

.create-comment-form {
    flex-direction: column;

}

.create-comment-button {
    border-radius: 0;
    border-top: 2px solid #36434d;
}

.input-image {
    display: none;
}

.input-file-svg {
    transition: .2s;
}

.input-file-svg:hover {
    transition: .1s;
    transform: rotate(20deg);
}
</style>