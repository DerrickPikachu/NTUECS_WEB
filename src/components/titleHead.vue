<template>
  <header>
    <HiddenImg></HiddenImg>
  </header>
</template>

<script>
import HiddenImg from "@/components/HiddenImg";

export default {
  name: "titleHead",
  components: {
    HiddenImg
  }
};
</script>

<style scoped>
header {
  position: relative;
  background-color: #FD7777;
  z-index: 2;
}
/*header h1 {*/
/*  font-size: 4em;*/
/*  text-transform: uppercase;*/
/*  text-align: center;*/
/*}*/
</style>