<template>
  <div id="base_menu_contaienr">
    <img
      id="base_menu_logo"
      alt="Tsugitasu Logo"
      src="../assets/logo.svg"
      @click="router_to('/')"
    />
    <div id="menu_link_container">
      <div class="menu_link" @click="router_to('/filter/')">
        <div class="border_animation" />
        <span class="link_text">教材・授業を探す</span>
      </div>
      <div class="menu_link" @click="router_to('/mypage/:uid/')">
        <div class="border_animation" />
        <span class="link_text">マイページ</span>
      </div>
      <div class="menu_link" @click="router_to('/login/')">
        <div class="border_animation" />
        <span :class="($route.path !== '/') ? 'active_link_text' : 'link_text'">ログイン</span>
      </div>
      <div class="signup_btn" @click="router_to('/signup/')">
        <span class="signup_text"> アカウント作成する </span>
        <div class="right_arrow_container">
          <img
            class="right_arrow"
            alt="right_arrow"
            src="../assets/icons/right_arrow.svg"
          />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: "App",
  components: {
    // MenubarIcon,
  },
  data() {
    return {
      // hamburger_menu_pos: -300,
    };
  },
  methods: {
    router_to (target) {
      this.$router.push(target);
    },
  },
};
</script>

<style lang="scss" scoped>
#base_menu_contaienr {
  background-color: #F8F8F8;
  width: 100%;
  height: 100px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  box-shadow: #72727229 0px 2px 7px;
  #base_menu_logo{
    cursor: pointer;
    width: 200px;
    margin-left: 20px;
  }
  #menu_link_container{
    margin-right: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    .menu_link {
      margin: 0 20px;
      cursor: pointer;
      font-size: 18px;
      font-weight: 600;
      position: relative;
      &:hover {
        color: #3EB595;
      }
      &:hover > .border_animation {
        width: 100%;
      }
      .border_animation {
        width: 0%;
        height: 100%;
        border-bottom: #3EB595 solid 3px;
        position: absolute;
        transition: 0.4s;
      }
      .link_text {
        color: #343434;
        transition: 0.1s;
      }
      .active_link_text {
        color: #3EB595;
        transition: 0.1s;
      }
    }
    .signup_btn {
      cursor: pointer;
      width: 240px;
      padding: 10px 15px;
      border-radius: 99px;
      background-color: #3EB595;
      font-size: 18px;
      font-weight: 600;
      color: #FFFFFF;
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-items: center;
      transition: 0.4s;
      position: relative;
      &:hover {
        background-color: #3b8a77;
      }
      &:hover > .right_arrow_container {
        width:35px;
      }
      .signup_text{
        height: 30px;
        display: flex;
        justify-content: center;
        align-items: flex-end;
      }
      .right_arrow_container{
        width: 28px;
        height: 28px;
        margin-left: 10px;
        border: #FFFFFF solid 2px;
        border-radius: 20px;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.2s;
        .right_arrow{
          width: 20px;
          height: 20px;
          transition: 0.2s;
        }
      }
      &:hover > .right_arrow_container > .right_arrow {
        width: 30px;
      }
    }
  }
}

</style>
