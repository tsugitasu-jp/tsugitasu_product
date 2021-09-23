<template>
  <div class="mypage_management_container">
    <div class="mypage_header">
      <h1>マイ教材・授業</h1>
      <p>あなたが作成した教材や授業を確認しましょう！</p>
    </div>
    <div class="materials_label_container">
      <div class="label">
        最近作成した教材
      </div>
      <div class="materials_container">
        <div class="material_container" v-for="my_material in disp_list.my_materials" :key="my_material.id" @click="touchToMaterial(my_material.cid, my_material.bid, my_material.ver)">
          <img class="material_image" :style="{ backgroundImage: 'url(/media/' + my_material.cid + '/b' + my_material.bid + '/v' + my_material.ver + '/' + my_material.content_image_main + ')' }">
          <div class="material_title">
            {{my_material.title.slice(0, 15)}}...
          </div>
          <div class="material_description">
            <p v-html="my_material.context.slice(0, 60) + '...' " style="display: block"></p>
          </div>
          <div class="author_container">
            <div class="author_name">
              {{my_material.display_name}}
            </div>
            <div class="author_date">
              {{my_material.created_at}}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="materials_label_container">
      <div class="label">
        お気に入りの教材
      </div>
      <div class="materials_container">
        <div class="material_container" v-for="favorite_material in disp_list.favorite_materials" :key="favorite_material.id">
          <img class="material_image" :src="favorite_material.image">
          <div class="material_title">
            {{favorite_material.title}}
          </div>
          <div class="material_description">
            {{favorite_material.description}}
          </div>
          <div class="author_container">
            <div class="author_name">
              {{favorite_material.author}}
            </div>
            <div class="author_date">
              {{favorite_material.auth_date}}
            </div>
          </div>
        </div>
      </div>
    </div>
    <FooterMenu />
  </div>
</template>

<script>
import FooterMenu from "../components/FooterMenu.vue";
var firebase = require('firebase/app')
require('firebase/auth')

export default {
  components: { 
    FooterMenu
  },
  data() {
    return {
      disp_list:{
        my_materials:[],
        favorite_materials:[
          {
            title:"教材タイトル",
            description:"EXPLAINーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー",
            author:"Tatsuya Okazaki",
            auth_date:"2020.01/01",
            image:"https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"
          },
          {
            title:"教材タイトル",
            description:"EXPLAINーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー",
            author:"Tatsuya Okazaki",
            auth_date:"2020.01/01",
            image:"https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"
          },
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
    firebase.default.auth().onAuthStateChanged((user) => {
      user.getIdToken().then((token) => {
        const config = {
          headers: {
            'Authorization': "JWT " + token,
          },
        };
        this.axios
          .get('/api-v1/contents/me/', config)
          .then((response) => {
            console.log(response.data)
            this.$set(this.disp_list, 'my_materials', response.data)
          })
          .catch(function(error) {
              console.log(error)
          })
      });
      
    })
  },
  computed: {
  },
  methods: {
    touchToMaterial(cid, bid, vid){
      console.log(cid)
      console.log(bid)
      console.log(vid)
      this.$router.push({ name: 'MaterialsDescription', params: {cid: cid, bid: bid, vid: vid}})
    },
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
    width: 80%;
    margin: 30px 0 15px 0;
    padding-left: 50px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
  }
  .materials_label_container{
    background-color: #F6F6F6;
    width: 80%;
    padding: 15px;
    margin: 25px 0;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    .label{
      padding: 10px 15px;
      font-size: 25px;
      font-weight: 600;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
    }
    .materials_container{
      background-color: #F6F6F6;
      width: 100%;
      max-height: 800px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;
      overflow-y: scroll;
      .material_container{
        cursor: pointer;
        flex-shrink: 0;
        width: 250px;
        height: 250px;
        margin: 15px;
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
}
</style>