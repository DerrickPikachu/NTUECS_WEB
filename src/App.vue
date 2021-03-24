<template>
  <Head />
  <NavBar></NavBar>
  <titleHead ref="header" id="header"></titleHead>
  <div id='nav-bg'></div>
  <section id='about'>
    <div class='container'>
<!--      <div style="height: 25em; background-color: darkseagreen"></div>-->
      <div style="height: 25em" class="informationBlock"></div>
<!--      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vel diam lacus. Nam quis ipsum nec massa sagittis scelerisque ac non urna. Phasellus posuere orci ac tellus interdum mollis eu vitae mi. Aliquam nec ante lobortis, suscipit lectus eu, dignissim ante. Nam imperdiet quis eros.</p>-->
    </div>
    <div class="container">
<!--      <div style="height: 25em; background-color: cornflowerblue"></div>-->
      <div style="height: 25em;" class="informationBlock"></div>
    </div>
    <div class="container">
<!--      <div style="height: 25em; background-color: indianred"></div>-->
      <div style="height: 25em" class="informationBlock"></div>
    </div>
  </section>
<!--  <test></test>-->
</template>

<script>
import titleHead from './components/titleHead.vue'
import NavBar from "@/components/NavBar";
// import HiddenImg from './components/HiddenImg.vue'
// import test from './components/test.vue'
import $ from 'jquery'

export default {
  name: 'App',
  components: {
    // test
    titleHead,
    NavBar
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
      console.log("calc: " + calc);

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
#about {
  background: #E7E3DA;
  /*height: 70em;*/
  padding: 5em 0;
}
#about p {
  line-height: 2em;
  font-size: 1.4em;
  margin: 0;
  color: #222;
}
.informationBlock {
  background-color: white;
  margin-top: 5em;
  border-radius: 5px;
}
</style>
