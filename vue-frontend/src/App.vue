<template>
  <div id = "app">
    <TitleHeader title = "Named Entity Recognition"/>
    <NerForm 
      @show-result = "showResult" 
      @clear-flag = "clearFlag" 
    />
    <NerResult 
      :results = "ner_result" 
      :flag = "flag"
    />
  </div>
</template>

<script>
import TitleHeader from './components/TitleHeader.vue'
import NerForm from './components/NerForm.vue'
import NerResult from './components/NerResult.vue'

export default {
  name: 'App',
  components: {
    TitleHeader,
    NerForm,
    NerResult
  },
  data() {
    return {
      ner_result : [],
      flag       : 0
    }
  },
  methods : { 
    showResult(response){
      this.ner_result = response.results;
      this.flag       = 1;
    },
    clearFlag(flag){
      this.flag = flag;
    }
  },
}
</script>

<style>
#app {
  font-family             : Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing  : antialiased;
  -moz-osx-font-smoothing : grayscale;
  text-align              : center;
  color                   : #2c3e50;
  margin-top              : 60px;
}
</style>
