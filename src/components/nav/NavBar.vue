<template>
  <nav>
    <div class='container'>
      <div class="logo"></div>
      <ul>
        <nav-tag v-for="tagInfo in navList" :nav-data="tagInfo" :key="tagInfo['tagName']"></nav-tag>
      </ul>
    </div>
  </nav>
</template>

<script>
import NavTag from "@/components/nav/navTag";
export default {
  name: "NavBar",
  components: {NavTag},
  data () {
    return {
      navList: [
        {
          tagName: '招生資訊',
          tags: [
            '學士',
            '碩士',
            '碩士在職'
          ]
        },
        {
          tagName: '訊息公告',
          tags: [
            '最新消息',
            '榮譽榜'
          ]
        },
        {
          tagName: '能力檢定',
          tags: [
            '資訊能力',
            'CPE'
          ]
        },
        {
          tagName: '系所簡介',
          tags: [
            '空間設備',
            '系所沿革',
            '教育目標',
            '特色'
          ]
        },
        {
          tagName: '師資陣容',
          tags: [
            '專任',
            '兼任',
            '退休',
            '行政'
          ]
        },
        {
          tagName: '法規',
          tags: [
            '行政',
            '大學部',
            '碩士班'
          ]
        }
      ]
    }
  },
}
</script>

<style scoped>
nav {
  position: fixed;
  width: 100%;
  margin: 0 auto;
  top: 0;
  z-index: 3;
  height: 5em;
}
nav:hover {
  background-color: #222;
  transition: all 0.5s;
}
nav ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
  float: right;
}
.logo {
  background: url("../../assets/logo.png") no-repeat;
  background-size: cover;
  float: left;
  height: 5em;
  width: 5em;
  z-index: 3;
}

/*nav li {*/
/*  display: inline-block;*/
/*  padding: 2em;*/
/*  text-align: center;*/
/*  transition: all 0.2s;*/
/*}*/
/*nav li:last-child {*/
/*  padding-right: 0;*/
/*}*/
/*nav a {*/
/*  color: #FFF;*/
/*  text-decoration: none;*/
/*  transition: all 0.3s;*/
/*}*/
/*nav a:hover {*/
/*  color: #DDD;*/
/*}*/
/*.dropdown-color {*/
/*  background: #222222;*/
/*}*/
/*.dropdown-color li {*/
/*  padding: 0;*/
/*  width: 100%;*/
/*}*/
/*.dropdown-color li a {*/
/*  padding-top: 1em;*/
/*  padding-bottom: 1em;*/
/*}*/
</style>