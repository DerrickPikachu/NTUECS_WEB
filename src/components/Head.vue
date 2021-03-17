<template>
  <nav class="w-100 myNav navbar navbar-expand-lg navbar-dark bg-dark justify-content-between">
    <a class="navbar-brand">PikaChin</a>
    <div class="form-inline">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item" v-for="text in navbar" :key="text">
            <a class="nav-link" href="#">{{ text }}</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Head",
  data () {
    return {
      navbar: [
          'Home',
          'About Me',
          'Education',
          'Interest'
      ]
    }
  }
};
</script>

<style scoped>
.myNav {
  position: fixed;
}
</style>