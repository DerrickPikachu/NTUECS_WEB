<template>
  <nav>
    <div class='container'>
      <div class="logo"></div>
      <ul>
        <li class="nav-item dropdown">
          <a class="dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" @click="dropdownHandle">
            Item 1
          </a>
          <ul class="dropdown-menu dropdown-color" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">something</a></li>
            <li><a class="dropdown-item" href="#">something2</a></li>
          </ul>
        </li>
        <li>
          <a href='#'>Item 2</a>
        </li>
        <li>
          <a href='#'>Item 3</a>
        </li>
        <li>
          <a href='#'>Item 4</a>
        </li>
        <li>
          <a href='#'>Item 5</a>
        </li>
        <li>
          <a href='#'>Item 6</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar"
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
nav li {
  display: inline-block;
  padding: 2em;
  text-align: center;
  transition: all 0.2s;
}
nav li:last-child {
  padding-right: 0;
}
nav a {
  color: #FFF;
  text-decoration: none;
  transition: all 0.3s;
}
nav a:hover {
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
.logo {
  background: url("../assets/logo.png") no-repeat;
  background-size: cover;
  float: left;
  height: 5em;
  width: 5em;
  z-index: 3;
}
</style>