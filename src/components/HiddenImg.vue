<template>
<!--  <img src="testImg.png" class="hiddenImg">-->
  <div class="w-100 title hiddenImg" id="mainTitle">
    <div class="container titleText d-flex text-center align-items-center">
      <div class="w-100">
        <h1>資訊科學系</h1>
        <p>國立臺北教育大學</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HiddenImg"
}
</script>

<style scoped>
.hiddenImg {
  /*position: fixed;*/
  background: url(../background.jpg) no-repeat center center fixed;
  background-size: cover;
  width: 100%;
  z-index: -100;
}
.sticky {
  padding: 0vh 0vw;
  position: fixed;
  z-index: 1000;
  height: 25vh;
  background-size: cover;
}
.title {
  padding: 25vh 0vw;
}
.titleText {
  height: 50vh;
  color: white;
}
.contentHeight {
  height: 25vh;
}
h1 {
  font-size: 4em;
  text-transform: uppercase;
  text-align: center;
}
</style>