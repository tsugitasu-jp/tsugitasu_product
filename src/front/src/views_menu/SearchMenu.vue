<template>
  <div class="menu_container">
    <div class="side_menu" :style="MenuStyle.Side">
      <div class="side_menu_header">
        <img class="side_logo" src="../assets/logo.svg" alt="side_logo" @click="router_to('/')">
        <img class="side_trg_icon" src="../assets/icons/close.svg" alt="side_trg_icon" @click="SideMenu_trg_icon_click">
      </div>
      <div class="side_menu_container" style="height:30%">
        <div class="header_text" :class="SideMenuHighlight.Search.header?'header_text_highlight':'header_text_no_highlight'">
          Search
        </div>
        <div class="link_container" @click="router_to('/filter/'); SideMenu_trg_icon_click()">
          <img v-if="SideMenuHighlight.Search.Material" class="link_img" src="../assets/icons/side_menu_black/search.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/search.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.Search.Material?'link_text_highlight':'link_text_no_highlight'">教材を探す</span>
        </div>
        <div class="link_container">
          <img v-if="SideMenuHighlight.Search.Lesson" class="link_img" src="../assets/icons/side_menu_black/folder.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/folder.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.Search.Lesson?'link_text_highlight':'link_text_no_highlight'">授業を探す</span>
        </div>
        <div class="link_container">
          <img v-if="SideMenuHighlight.Search.idea" class="link_img" src="../assets/icons/side_menu_black/idea.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/idea.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.Search.idea?'link_text_highlight':'link_text_no_highlight'">アイデアと出会う</span>
        </div>
      </div>
      <div class="side_menu_container" style="height:40%">
        <div class="header_text" :class="SideMenuHighlight.MySpace.header?'header_text_highlight':'header_text_no_highlight'">
          My Space
        </div>
        <div class="link_container" @click="mymanagement(); SideMenu_trg_icon_click()">
          <img v-if="SideMenuHighlight.MySpace.Material" class="link_img" src="../assets/icons/side_menu_black/book-open.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/book-open.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.MySpace.Material?'link_text_highlight':'link_text_no_highlight'">マイ教材・授業</span>
        </div>
        <div class="link_container" @click="myupload(); SideMenu_trg_icon_click()">
          <img v-if="SideMenuHighlight.MySpace.Upload" class="link_img" src="../assets/icons/side_menu_black/paper-plane.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/paper-plane.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.MySpace.Upload?'link_text_highlight':'link_text_no_highlight'">投稿・アップロード</span>
        </div>
        <div class="link_container">
          <img v-if="SideMenuHighlight.MySpace.Manage" class="link_img" src="../assets/icons/side_menu_black/project.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/project.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.MySpace.Manage?'link_text_highlight':'link_text_no_highlight'">教材・授業管理</span>
        </div>
        <div class="link_container" @click="myaccount(); SideMenu_trg_icon_click()">
          <img v-if="SideMenuHighlight.MySpace.Account" class="link_img" src="../assets/icons/side_menu_black/settings.svg" alt="search_icon_black">
          <img v-else class="link_img" src="../assets/icons/side_menu_gray/settings.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.MySpace.Account?'link_text_highlight':'link_text_no_highlight'">マイアカウント</span>
        </div>
      </div>
      <div class="side_menu_container" style="height:20%">
        <div class="header_text" :class="SideMenuHighlight.Other.header?'header_text_highlight':'header_text_no_highlight'">
          Other
        </div>
        <div class="link_container">
          <img v-if="SideMenuHighlight.Other.Help" class="link_img" src="../assets/icons/side_menu_black/help-circle-outline.svg" alt="search_icon_black">
          <img else class="link_img" src="../assets/icons/side_menu_gray/help-circle-outline.svg" alt="search_icon_black">
          <span class="link_text" :class="SideMenuHighlight.Other.Help?'link_text_highlight':'link_text_no_highlight'">ヘルプ・お問い合わせ</span>
        </div>
      </div>
    </div>
    <div class="search_menu_contaienr" :style="MenuStyle.Header">
      <img class="side_trg_icon" src="../assets/icons/open.svg" alt="side_trg_icon" @click="SideMenu_trg_icon_click">
      <div class="search_box_container">
        <input class="search_box" type="text" placeholder="検索項目を入力">
        <img class="search_icon" src="../assets/icons/search-icon.svg" alt="search-icon">
      </div>
      <div id="menu_link_container">
        <div class="description_search_btn" @click="router_to('/filter/')">
          <div class="description_search_btn_icon">
            <img
              class="pink_sankaku_icon"
              alt="description_search_btn_icon"
              src="../assets/icons/pink_sankaku.svg"
            />
            <img
              class="white_sankaku_icon"
              alt="description_search_btn_icon"
              src="../assets/icons/white_sankaku.svg"
            />
          </div>
          <span class="description_search_btn_text">詳細検索</span>
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
  </div>
</template>

<script>
var firebase = require('firebase/app')
require('firebase/auth')

export default {
  name: "App",
  components: {
    // MenubarIcon,
  },
  data() {
    return {
      MenuStyle: {
        SideIsDisp : false,
        Side : "left:-300px;",
        Header : "width:100%;",
      },
      SideMenuHighlight: {
        Search: {
          header: false,
          Material: false,
          Lesson: false,
          Idea: false,
        },
        MySpace: {
          header: false,
          Material: false,
          Upload: false,
          Manage: false,
          Account: false,
        },
        Other: {
          header:false,
          Help: false,
        }
      }
    };
  },
  created() {
    this.SideMenu_Highlight_Init();
  },
  watch: {
    $route() {
      this.SideMenu_Highlight_Init();
    }
  },
  methods: {
    router_to (target) {
      this.$router.push(target);
    },
    SideMenu_trg_icon_click() {
      if (this.MenuStyle.SideIsDisp) {
        this.MenuStyle.Side = "left:-300px;";
        this.MenuStyle.Header = "width:100%;";
      } else {
        this.MenuStyle.Side = "left:0px;";
        this.MenuStyle.Header = "width:calc(100% - 240px);";
      }
      this.MenuStyle.SideIsDisp = !this.MenuStyle.SideIsDisp;
    },
    SideMenu_Highlight_Init() {
      console.log(this.$route.name)
      this.SideMenu_Highlight_Clear();
      if(this.$route.name === 'Filter' || this.$route.name === 'MaterialsDescription') {
        this.SideMenuHighlight.Search.header = true;
        this.SideMenuHighlight.Search.Material = true;
      }else if(this.$route.name === 'MyPage'){
        this.SideMenuHighlight.MySpace.header = true;
        this.SideMenuHighlight.MySpace.Account = true;
      }else if(this.$route.name === 'MyPageManagement'){
        this.SideMenuHighlight.MySpace.header = true;
        this.SideMenuHighlight.MySpace.Material = true;
      }else if(this.$route.name === 'MyPageUpload'){
        this.SideMenuHighlight.MySpace.header = true;
        this.SideMenuHighlight.MySpace.Upload = true;
      }
    },
    SideMenu_Highlight_Clear() {
      this.SideMenuHighlight = {
        Search: {
          header: false,
          Material: false,
          Lesson: false,
          Idea: false,
        },
        MySpace: {
          header: false,
          Material: false,
          Upload: false,
          Manage: false,
          Account: false,
        },
        Other: {
          header:false,
          Help: false,
        }
      }
    },
    myaccount(){
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          this.router_to("/mypage/" + user.uid);
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
    myupload(){
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          this.router_to("/mypage/" + user.uid + "/upload");
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
    mymanagement(){
      var unsubscribe = firebase.default.auth().onAuthStateChanged(user => {
        if (user){
          this.router_to("/mypage/" + user.uid + "/management");
        }else{
          location.reload();
        }
        unsubscribe();
      });
    },
  },
}
</script>

<style lang="scss" scoped>
.menu_container{
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  .side_menu{
    background-color: #F8F8F8;
    width: 300px;
    height: 100%;
    padding-left: 20px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    position: fixed;;
    z-index: 1000;
    box-shadow: #72727221 2px 0 7px;
    transition: 0.2s;
    pointer-events: auto;
    .side_menu_header{
      width: 100%;
      height: 100px;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      .side_logo{
        cursor: pointer;
        height: 35px;
      }
      .side_trg_icon{
        cursor: pointer;
        width: 30px;
        height: 30px;
        margin-right: 20px;
      }
    }
    .side_menu_container{
      width: 100%;
      background-color: #F8F8F8;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      .header_text{
        font-size: 30px;
        font-weight: 700;
        transition: 0.2s;
      }
      .header_text_highlight{
        color: #3EB595;
      }
      .header_text_no_highlight{
        color: #AAAAAA;
      }
      .link_container{
        cursor: pointer;
        width: 100%;
        height: 40px;
        margin: 15px 0;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        .link_img{
          width: 25px;
          height: 25px;
          margin: 0 20px;
          transition: 0.2s;
        }
        .link_text{
          font-size: 16px;
          font-weight: 700;
          transition: 0.2s;
        }
        .link_text_highlight{
          color: #000000;
        }
        .link_text_no_highlight{
          color: #AAAAAA;
        }
      }
    }
  }
  .search_menu_contaienr {
    background-color: #FFFFFF;
    // width: calc(100% - 240px);
    height: 100px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    box-shadow: #72727229 0px 2px 7px;
    position: fixed;
    right: 0px;
    pointer-events: auto;
    transition: 0.2s;
    .side_trg_icon {
      width: 30px;
      height: 30px;
      margin-left: 20px;
      cursor: pointer;
    }
    .search_box_container {
      flex: 1;
      margin: 0 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      .search_box{
        outline: none;
        border: 2px solid #EAEAEA;
        border-radius: 15px;
        width: 100%;
        height: 50px;
        padding: 0 10px 0 60px;
      }
      .search_icon{
        width: 25px;
        height: 25px;
        position: absolute;
        left: 25px;
      }
    }
    #menu_link_container{
      margin-right: 30px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      .description_search_btn{
        cursor: pointer;
        width: 130px;
        padding: 8px 10px;
        border-radius: 10px;
        background-color: #FFFFFF;
        border: 2px solid #F23D75;
        color: #F23D75;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.2s;
        .description_search_btn_icon{
          width: 20px;
          height: 17px;
          margin-top: 3px;
          position: relative;
          img {
            position: absolute;
            transition: 0.2s;
          }
          .white_sankaku_icon{
            opacity: 0;
          }
          .pink_sankaku_icon{
            opacity: 1;
          }
        }
        .description_search_btn_text{
          margin-left: 10px;
          font-size: 16px;
          font-weight: 600;
        }
        &:hover{
          background-color: #F23D75;
          color: #FFFFFF;
        }
        &:hover > .description_search_btn_icon > .white_sankaku_icon{
          opacity: 1;
        }
        &:hover > .description_search_btn_icon > .pink_sankaku_icon{
          opacity: 0;
        }
      }
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
}

</style>
