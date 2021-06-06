<!--<template>-->
<!--  <div id="nav">-->
<!--    <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About</router-link>-->
<!--  </div>-->
<!--  <router-view/>-->
<!--</template>-->
<template>
  <NavBar></NavBar>
  <titleHead ref="header" id="header"></titleHead>
  <div id='nav-bg'></div>
  <about></about>
<!--  <test></test>-->
</template>

<script>
// import HiddenImg from './components/HiddenImg.vue'
// import test from './components/test.vue'
import $ from 'jquery'
import titleHead from './components/titleHead.vue';
import NavBar from "@/components/nav/NavBar";
import about from "@/components/about";
export default {
  name: 'App',
  components: {
    // test
    titleHead,
    NavBar,
    about
    // HiddenImg
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  unmounted() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  data() {
    return {
      range: 200
    }
  },
  methods: {
    handleScroll: function() {
      var header = document.getElementById("header");
      var scrollTop = window.scrollY,
          height = header.clientHeight,
          calc = 1 - (scrollTop / height);
      // console.log("calc: " + calc);
      if (calc > 1) {
        header.style.opacity = '1';
      } else if (calc < 0) {
        header.style.opacity = '0';
      } else {
        header.style.opacity = '' + calc;
      }
    }
  }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Montserrat:400,700);
@import url(http://weloveiconfonts.com/api/?family=fontawesome);
[class*=fontawesome-]:before {
  font-family: "FontAwesome", sans-serif;
}
* {
  box-sizing: border-box;
}
*:before, *:after {
  box-sizing: border-box;
}
body {
  background: #222;
  margin: 0;
  font-family: "Montserrat", sans-serif;
  font-size: 16px;
  color: #FFF;
}
/*.container {*/
/*  max-width: 60em;*/
/*  min-width: 45em;*/
/*  margin: 0 auto;*/
/*  padding: 0 2em;*/
/*}*/
#nav-bg {
  background: #222;
  position: fixed;
  height: 5em;
  width: 100%;
  top: 0;
  z-index: 1;
}
</style>

