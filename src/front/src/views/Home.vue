<template>
  <div class="login_container">
    <FooterMenu />
  </div>
</template>

<script>
import FooterMenu from "../components/FooterMenu.vue";

export default {
  components: { 
    FooterMenu
  },
  data() {
    return {
    };
  },
  created() {
  },
  computed: {
  },
  methods: {
    
  },
};
</script>

<style lang="scss" scoped>
.login_container{
  background-color: #F8F8F8;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>