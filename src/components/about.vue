<template>
  <section id='about'>
    <div class='container'>
<!--      <div style="height: 25em" class="informationBlock"></div>-->
      <lesson-info></lesson-info>
    </div>
    <div class="container mt-5">
<!--      <div style="height: 25em;" class="informationBlock"></div>-->
      <master-section></master-section>
    </div>
    <div class="container">
      <div style="height: 25em" class="informationBlock"></div>
    </div>
  </section>
</template>

<script>
import lessonInfo from "@/components/lesson/lessonInfo";
import masterSection from "@/components/master-section/masterSection";
export default {
  name: "about",
  components: {
    masterSection,
    lessonInfo,
  }
}
</script>

<style scoped>
#about p {
  line-height: 2em;
  font-size: 1.4em;
  margin: 0;
  color: #222;
}
.informationBlock {
  /*background-color: white;*/
  margin-top: 2em;
  border-radius: 5px;
  border: 2px;
}
#about {
  background: #E7E3DA;
  /*height: 70em;*/
  padding: 2em 0 5em 0;
}
</style>