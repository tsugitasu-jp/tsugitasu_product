<template>
  <div class="userinfo_container">
    <div class="profile_container">
      <div class="profile_image">
      </div>
      <div class="profile_description">
        <div class="user_name">
          ユーザーネーム
        </div>
        <div class="role">
          肩書き / 教員 / 野球部顧問 / 進路指導部長
        </div>
        <div class="content_number_container">
          <div class="content_number">
            <div class="number">
              12
            </div>
            <div class="label">
              教材・授業
            </div>
          </div>
          <div class="content_number">
            <div class="number">
              12
            </div>
            <div class="label">
              フォロワー
            </div>
          </div>
          <div class="content_number">
            <div class="number">
              12
            </div>
            <div class="label">
              フォロー中
            </div>
          </div>
        </div>
        <div class="intro_container">
          <p>一児の父です。</p>
          <p>名古屋市の中学校で2年の担当をしています。</p>
          <p>野球部の顧問です。</p>
          <p>練習試合の相手も募集中です↓</p>
          <p>example@example.com</p>
          <p>数学担当</p>
        </div>
        <div class="edit_btn">
          フォローする
        </div>
      </div>
    </div>
    <div class="materials_follow_follower_btn_container">
      <div class="materials_follow_follower_btn" :style="style.btn.materials" @click="btn_style_change ('materials')">
        <div>
          教材・授業
        </div>
      </div>
      <div class="materials_follow_follower_btn" :style="style.btn.follower" @click="btn_style_change ('follower')">
        <div>
          フォロワー
        </div>
      </div>
      <div class="materials_follow_follower_btn" :style="style.btn.follow" @click="btn_style_change ('follow')">
        <div>
          フォロー中
        </div>
      </div>
    </div>
    <div class="materials_follow_follower_container">
      <div class="materials_list_container" :style="style.box.materials">
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
      <div class="materials_follow_follower_list_container" :style="style.box.follower">
        <div class="label">
          フォロワー
        </div>
        <div class="materials_follow_follower" v-for="follower in disp_list.follower" :key="follower.id">
          <div class="user_info_btn">
            <div class="user_image">
            </div>
            <div class="user_name">
              {{follower.username}}
            </div>
          </div>
          <div class="user_info_btn">
            <div class="materials">
              {{follower.materials}}
            </div>
            <div class="user">
              {{follower.follower}}
            </div>
            <div class="btn">
              フォローする
            </div>
          </div>
        </div>
      </div>
      <div class="materials_follow_follower_list_container" :style="style.box.follow">
        <div class="label">
          フォロー中のユーザー
        </div>
        <div class="materials_follow_follower" v-for="follow in disp_list.follow" :key="follow.id">
          <div class="user_info_btn">
            <div class="user_image">
            </div>
            <div class="user_name">
              {{follow.username}}
            </div>
          </div>
          <div class="user_info_btn">
            <div class="materials">
              {{follow.materials}}
            </div>
            <div class="user">
              {{follow.follower}}
            </div>
            <div class="btn_unfollow">
              フォロー解除
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
        follower:[
          {
            username:"フォロワーユーザーネーム",
            materials:25,
            follower:12
          },
        ],
        follow:[
          {
            username:"フォローユーザーネーム",
            materials:35,
            follower:42
          },
        ]
      },
      style:{
        btn:{
          materials:"background-color: #F23D75;color: #FFFFFF;",
          follower:"background-color: transparent;color: #000000;",
          follow:"background-color: transparent;color: #000000;",
        },
        box:{
          materials:"left: 0px;",
          follower:"left: 1000px;",
          follow:"left: 2000px;",
        }
      }
    };
  },
  created() {
  },
  computed: {
  },
  methods: {
    btn_style_change (btn_kinds) {
      if(btn_kinds == "materials"){
        this.style.btn.materials = "background-color: #F23D75;color: #FFFFFF;";
        this.style.box.materials = "left:0px";
        this.style.btn.follow = "background-color: transparent;color: #000000;";
        this.style.box.follow = "left:1000px";
        this.style.btn.follower = "background-color: transparent;color: #000000;";
        this.style.box.follower = "left:2000px";
        
      }else if(btn_kinds == "follow"){
        this.style.btn.materials = "background-color: transparent;color: #000000;";
        this.style.box.materials = "left:-2000px";
        this.style.btn.follow = "background-color: #F23D75;color: #FFFFFF;";
        this.style.box.follow = "left:0px";
        this.style.btn.follower = "background-color: transparent;color: #000000;";
        this.style.box.follower = "left:-1000px";
        
      }else if(btn_kinds == "follower"){
        this.style.btn.materials = "background-color: transparent;color: #000000;";
        this.style.box.materials = "left:-1000px";
        this.style.btn.follow = "background-color: transparent;color: #000000;";
        this.style.box.follow = "left:1000px";
        this.style.btn.follower = "background-color: #F23D75;color: #FFFFFF;";
        this.style.box.follower = "left:0px";
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.userinfo_container{
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .profile_container{
    background: transparent linear-gradient(160deg, #F6F6F6 0%, #FFFFFF 100%) 0% 0% no-repeat padding-box;
    width: 1000px;
    height: 700px;
    margin: 30px 0;
    border-radius: 15px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    .profile_image{
      background-color: brown;
      width: 400px;
      height: 700px;
      border-radius: 15px 0 0 15px;
    }
    .profile_description{
      width: 600px;
      height: 700px;
      padding: 20px;
      border-radius: 0 15px 15px 0;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      .user_name{
        font-size: 40px;
        font-weight: 900;
      }
      .role{
        font-size: 20px;
        font-weight: 600;
      }
      .content_number_container{
        margin: 40px 0;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        .content_number{
          margin-right: 50px;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          .number{
            font-size: 50px;
            font-weight: 900;
          }
          .label{
            font-size: 15px;
            font-weight: 900;
          }
        }
      }
      .intro_container{
        width: 90%;
        height: 200px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        overflow-y: scroll;
        p{
          font-size: 19px;
          font-weight: 600;
        }
      }
      .edit_btn{
        margin-top: 50px;
        cursor: pointer;
        background-color: #F23D75;
        width: 150px;
        height: 45px;
        border-radius: 13px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 600;
        color: #FFFFFF;
        transition: 0.2s;
        &:hover{
          background-color: #d22258;
        }
      }
    }
  }
  .materials_follow_follower_btn_container{
    width: 1000px;
    height: 100px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    .materials_follow_follower_btn{
      cursor: pointer;
      border-radius: 99px;
      width: 180px;
      height: 40px;
      margin: 0 20px;
      font-size: 20px;
      font-weight: 600;
      flex-direction: row;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: 0.2s;
    }
  }
  .materials_follow_follower_container{
    width: 1000px;
    height: 700px;
    overflow:hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    .materials_list_container{
      width: 1000px;
      height: 700px;
      padding: 0 50px;
      overflow-y: scroll;
      position: absolute;
      transition: 0.2s;
      display: flex;
      flex-direction: row;
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
    .materials_follow_follower_list_container{
      width: 1000px;
      height: 700px;
      overflow-y: scroll;
      position: absolute;
      transition: 0.4s;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      .label{
        flex-shrink: 0;
        margin: 20px;
        font-size: 25px;
        font-weight: 600;
      }
      .materials_follow_follower{
        flex-shrink: 0;
        width: 100%;
        height: 80px;
        border-bottom: 1px solid #222222;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        .user_info_btn{
          margin: 0 40px;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: center; 
          .user_image{
            width: 50px;
            height: 50px;
            margin-right: 20px;
            border-radius: 99px;
            background-color: red;
          }
          .user_name{
            font-size: 20px;
            font-weight: 600;
          }
          .materials{
            margin: 0 25px;
            font-size: 20px;
            font-weight: 600;
            color: #AAAAAA;
          }
          .user{
            margin: 0 25px;
            font-size: 20px;
            font-weight: 600;
            color: #AAAAAA;
          }
          .btn{
            cursor: pointer;
            margin-left:40px;
            width: 150px;
            height: 45px;
            border-radius: 13px;
            font-size: 20px;
            font-weight: 600;
            background-color: #F23D75;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
            &:hover{
              background-color: #d22258;
            }
          }
          .btn_unfollow{
            cursor: pointer;
            margin-left:40px;
            width: 150px;
            height: 45px;
            border: 2px solid #F23D75;
            border-radius: 13px;
            font-size: 20px;
            font-weight: 600;
            background-color: #FFFFFF;
            color: #F23D75;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
          }
        }
      }
    }
  }
}
</style>