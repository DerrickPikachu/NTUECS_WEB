<template>
  <div class="row w-100">
    <div v-for="tag in tagList" class="col-4 btn btn-2" @click="sectionTag = tag">{{ tagName[tag] }}</div>
  </div>
  <div class="sectionBorder">
    <course v-if="sectionTag === 'course'"></course>
    <useful-form v-if="sectionTag === 'usefulForm'"></useful-form>
  </div>
</template>

<script>
import course from "@/components/lesson/lessonTag/course";
import usefulForm from "@/components/lesson/lessonTag/usefulForm";

export default {
  name: "lessonInfo",
  components: {
    course,
    usefulForm,
  },
  data () {
    return {
      sectionTag: 'course',
      tagList: ['course', 'usefulForm', 'subjectSystem'],
      tagName: {
        'course': '課程架構',
        'usefulForm': '常用表單',
        'subjectSystem': '選課系統'
      }
    }
  },
}
</script>

<style scoped>
.sectionBorder {
  border-radius: 10px;
  border: 2px solid #FFF;
}
.col-4 {
  text-align: center;
  color: black;
}
@import url(https://fonts.googleapis.com/css?family=Roboto:400,100,900);
* {
  box-sizing: inherit;
  transition-property: all;
  transition-duration: 0.6s;
  transition-timing-function: ease;
}
.btn {
  color: #222;
  cursor: pointer;
  font-weight: 400;
  line-height: 45px;
  text-decoration: none;
  text-transform: uppercase;
}
.btn:hover {
  text-decoration: none;
}
.btn-2 {
  letter-spacing: 0;
}

.btn-2:hover,
.btn-2:active {
  letter-spacing: 5px;
}

.btn-2:after,
.btn-2:before {
  -webkit-backface-visibility: hidden;
          backface-visibility: hidden;
  border: 1px solid rgba(255, 255, 255, 0);
  bottom: 0px;
  content: " ";
  display: block;
  margin: 0 auto;
  position: relative;
  transition: all 280ms ease-in-out;
  width: 0;
}

.btn-2:hover:after,
.btn-2:hover:before {
  -webkit-backface-visibility: hidden;
          backface-visibility: hidden;
  border-color: #fff;
  transition: width 350ms ease-in-out;
  width: 70%;
}

.btn-2:hover:before {
  bottom: auto;
  top: 0;
  width: 70%;
}
</style>