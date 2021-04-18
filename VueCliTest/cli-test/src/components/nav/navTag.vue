<template>
  <li class="nav-item dropdown">
    <a class="dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
      {{navData['tagName']}}
    </a>
    <ul class="dropdown-menu dropdown-color" aria-labelledby="navbarDropdown">
      <li v-for="tag in navData['tags']" :key="tag">
        <a class="dropdown-item" href="#">
          {{tag}}
        </a>
      </li>
    </ul>
  </li>
</template>

<script>
export default {
  name: "navTag",
  props: ["navData"],
}
</script>

<style scoped>
li {
  display: inline-block;
  padding: 2em;
  text-align: center;
  transition: all 0.2s;
}
li:last-child {
  padding-right: 0;
}
a {
  color: #FFF;
  text-decoration: none;
  transition: all 0.3s;
}
a:hover {
  color: #DDD;
}
.dropdown-color {
  background: #222222;
}
.dropdown-color li {
  padding: 0;
  width: 100%;
}
.dropdown-color li a {
  padding-top: 1em;
  padding-bottom: 1em;
}
.dropdown-color li a:hover {
  color: #222;
}
</style>