<template>
  <div class="mypage_management_container">
    <div class="mypage_header">
      <h1>マイ教材・授業</h1>
      <p>あなたが作成した教材や授業を確認しましょう！</p>
    </div>
    <div class="my_materials_container">
      <div class="material_container" v-for="material in disp_list.materials" :key="material.id">
        <img class="material_image" :src="material.image">
        <div class="material_title">
          {{material.title}}
        </div>
        <div class="material_description">
          {{material.description}}
        </div>
        <div class="author_container">
          <div class="author_name">
            {{material.author}}
          </div>
          <div class="author_date">
            {{material.auth_date}}
          </div>
        </div>
      </div>
    </div>
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
      disp_list:{
        materials:[
          {
            title:"教材タイトル",
            description:"EXPLAINーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー",
            author:"Tatsuya Okazaki",
            auth_date:"2020.01/01",
            image:"https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"
          },
        ],
      }
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
.mypage_management_container{
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .mypage_header{
    width: 90%;
    margin: 20px 0;
    padding-left: 50px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
  }
  .my_materials_container{
    background-color: #F6F6F6;
    width: 90%;
    height: 1000px;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    flex-wrap: wrap;
    .material_container{
      cursor: pointer;
      flex-shrink: 0;
      width: 250px;
      height: 250px;
      margin: 25px;
      border: 1px solid #757474;
      border-radius: 10px;
      background-color: #ffffff;
      box-shadow: #75747455 1px 1px 5px;
      transition: 0.2s;
      &:hover{
        box-shadow: #757474 3px 3px 0px;
        position: relative;;
        top: -3px;
        left: -3px;
      }
      .material_image{
        border-radius: 10px 10px 0 0;
        width: 250px;
        height: 140px;
      }
      .material_title{
        font-size: 15px;
        font-weight: 500;
        padding: 0 10px;
      }
      .material_description{
        width: 100%;
        height: 60px;
        font-size: 11px;
        font-weight: 400;
        padding: 0 10px;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: flex-start;
      }
      .author_container{
        font-size: 10px;
        font-weight: 400;
        padding: 0 10px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
      }
    }
  }
}
</style>