<template>
  <div class="row">
    <div class="col-4">
      <div class="card border-dark">
        <a href="#">
          <img src="../../testImg.png" class="card-img-top" alt="...">
          <div class="card-body" id="master">
            <p class="card-text">
              <span class="code">&lt;</span>
              碩士班口試
              <span class="code">&#47;&gt;</span>
            </p>
          </div>
        </a>
      </div>
    </div>
    <div class="col-8">
      <div class="card border-dark mb-3">
        <div class="card-header">Header</div>
        <div class="card-body text-dark">
          <h5 class="card-title">Dark card title</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
name: "masterSection"
}
</script>

<style scoped>
p {
  margin: 0;
  color: #222;
}

h {
  color: #222;
}

a {
  text-decoration: none;
}

a:hover .code {
  color: #DDDDDD;
  transition: 0.5s;
}

.card {
  width: 100%;
}

.card-header {
  color: #222;
  font-size: 20px;
}

.card-text {
  text-align: center;
}

.code {
  color: #222222;
}

@media (max-width: 1000px) {
  .row {
    display: block;
  }

  .col-4 {
    width: 100%;
  }

  .col-8 {
    width: 100%;
    margin: 50px auto;
  }
}

#master {
  background-color: #222;
}

#master p {
  color: #DDDDDD;
  font-size: 20px;
}
</style>