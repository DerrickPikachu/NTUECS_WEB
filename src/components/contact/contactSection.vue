<template>
  <footer>
    <div class="container">
      <div class="mx-auto info">
        <img src="../../assets/logo.png">
        <div class="contactInfo">
          <p v-for="info in contactInfo" :key="info">{{info}}</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "contactSection",
  data () {
    return {
      contactInfo: [
          "網站著作權屬於 國立臺北教育大學資訊科學系",
          "電話\t(02)2732-1104 #63326 #63327",
          "網址\thttp://www.cs.ntue.edu.tw",
          "地址\t臺北市大安區和平東路二段134號 科學館B503\n",
          "維護\t系辦的工讀生們\n"
      ]
    }
  }
}
</script>

<style scoped>
footer {
  background-color: #222222;
  color: #DDDDDD;
  width: 100%;
  margin: 10px 0 0 0;
}

p {
  margin-bottom: 5px;
}

img {
  width: 150px;
  /*display: inline-block;*/
  margin-top: 0;
  margin-bottom: 0;
}

.info {
  width: 50%;
  display: flex;
  flex-direction: row;
}

.contactInfo {
  /*display: inline-block;*/
}

</style>