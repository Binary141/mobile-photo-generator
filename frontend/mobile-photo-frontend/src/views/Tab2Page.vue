<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <!-- <img @src="imageUrl"> -->
      <div  v-for="(image) in imageArray" style="display: block; display: flex; justify-content: center;" :key="image">
          <figure>
            <img class="galleryImages" v-bind:src="image" :key="image">
            <span class="caption">{{image}}</span>
          </figure>
      </div>
    </ion-content>
  </ion-page>
</template>

<style>
  figure { position: relative; display: block; overflow: hidden; }
  figure:hover img { opacity: .5; }
  figure img { max-width: 100% }
  figure .caption { position: absolute; display: block; top: 0; left: 0; height: 100%; width: 100%; opacity: 0; transition: all .2s ease-in-out }
  figure:hover .caption { opacity: 1;}
</style>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonPage, IonContent } from '@ionic/vue';

export default defineComponent({
  name: 'Tab2Page',
  components: { IonContent, IonPage },
  mounted: async function(){
      console.log("This was autoloaded!");
      let url = "defaultURL"
      // "http://code.binary141.com:6969/ListImages/"
      let response = await fetch("https://codes.binary141.com/ListImages", {
          method: "GET",
          headers: {},
      })

      let data = await response.json()
          this.imageLength = data["images"].split(",").length
          this.imageArray = data["images"].split(",")
  },
  methods: {
    getImages: function() {
      fetch("/ListImages").then(function (data) {
          console.log("images?: ", data);
      })
    },
  },
  data(){
    return{
      input: '',
      imageUrl: '',
      imageLength: 0,
      imageArray: [],
      size: 1
    }
  }

});
</script>
