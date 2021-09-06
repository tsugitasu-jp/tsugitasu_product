<template>
  <div class="materials_description_container">
    <div class="materials_main_description">
      <div class="materials_main_description_image">
      </div>
      <div class="materials_main_description_text">
        <div class="materials_main_description_text_title">
          小学校1年生 数の数え方と足し算
        </div>
        <div class="materials_main_description_text_tags_container">
          <div class="star_tag">
            ★ 2021
          </div>
          <div class="material_tag">
            足し算
          </div>
          <div class="material_tag">
            算数入門
          </div>
        </div>
        <div class="materials_main_description_text_date">
          2020.1.25
        </div>
        <div class="materials_main_description_text_description">
          <p>小学生１年生の算数の教育に入る前の数の概念を教える際に使う教材です。</p>
          <p>かわいいイラストを用いて、自動の皆に興味を持ってもらえるように工夫しています。学校現場だけでなく、家庭等でも使ってもらえると嬉しいです。</p>
          <p>テンポよくスライドと一緒に児童には答えてもらうような使い方を授業では想定しています。</p>
        </div>
        <div class="materials_main_description_text_author">
          <div class="author">
            Tatsuya Okazaki
          </div>
          <div class="follow_btn">
            + 作成者をフォロー
          </div>
        </div>
      </div>
    </div>
    <div class="materials_slide_description_container">
      <div class="slide">
        1
      </div>
      <div class="slide">
        2
      </div>
      <div class="slide">
        3
      </div>
    </div>
    <div class="btn_container">
      <div class="base_btn_style keep_btn">
        マイページにキープする
      </div>
      <div class="base_btn_style dl_btn">
        この教材をダウンロード
      </div>
      <div class="base_btn_style comment_btn">
        作者のコメントを送る
      </div>
    </div>
    <div class="comments_content_container">
      <div class="comment_label_container">
        <div class="comment_label">
          コメント
        </div>
        <div class="comment_number">
          12
        </div>
      </div>
      <div class="comments_container">
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
        <div class="comment_container">
          <div class="author_container">
            <div class="author_image">
            </div>
            <div class="name_date_container">
              <div class="name">
                Tatsuya Okazaki
              </div>
              <div class="date">
                5日前
              </div>
            </div>
          </div>
          <div class="comments_description">
            <p>かわいいイラストと楽しめる教材ですね！来月の授業で１年生に使ってみようと思います。</p>
            <p>あと少しだけ意見させてください。ところどころ小学生が読めないような漢字が使われているスライドがいくつか見受けられます。そこを修正すると良いと思います。</p>
          </div>
        </div>
      </div>
    </div>
    <div class="branch_container">
      <div class="branch_label_container">
        <div class="branch_label">
          <div class="label">
            この教材の状況を確認する
          </div>
          <div class="update_number">
            現在 <span style="color:#51B1F3;">4つ</span>のアップデート版が存在します
          </div>
        </div>
        <div class="material_title">
          小学校１年生向け「数の数え方と足し算」
        </div>
        <div class="now_watchng">
          最新版を閲覧しています
        </div>
      </div>
      <div class="branch_tree_container">
        <div class="own_material">
          <div class="own_material_image">
            スライド
          </div>
          <div class="own_material_title">
            <div class="left_top" />
            <div class="right_top" />
            <div class="right_bottom" />
            <div class="left_bottom" />
            <p>オリジナル</p>
          </div>
        </div>
        <div class="branch_materials_cotainer">
          <div class="branch_materials_row_cotainer" v-for="materials_row in disp_branch" :key="materials_row.id">
            <div class="branch_materials_container" v-for="materials in materials_row" :key="materials.id">
              <div class="branch_border_container">
                <div v-if="materials.top" class="top" />
                <div v-if="materials.right" class="right" />
                <div v-if="materials.left" class="left" />
                <div v-if="materials.bottom" class="bottom" />
              </div>
              <div class="branch_material_title">
                <div v-if="materials.title != ''" class="left_top" />
                <div v-if="materials.title != ''" class="right_top" />
                <div v-if="materials.title != ''" class="right_bottom" />
                <div v-if="materials.title != ''" class="left_bottom" />
                <p v-if="materials.title != ''" >{{materials.title}}</p>
                <div v-if="materials.title != ''" class="branch_material_author">
                  <div class="author_image">
                  </div>
                  <div class="author_date_container">
                    <div class="author">
                      {{materials.author}}
                    </div>
                    <div class="date">
                      {{materials.date}}
                    </div>
                  </div>
                </div>
              </div>
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
      disp_branch:[
        [
          {
            top:false,
            right:true,
            bottom:true,
            left:true,
            title:"教材1-1",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
          {
            top:false,
            right:true,
            bottom:true,
            left:true,
            title:"教材1-2",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
          {
            top:false,
            right:true,
            bottom:true,
            left:true,
            title:"教材1-3",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
          {
            top:false,
            right:true,
            bottom:false,
            left:true,
            title:"教材1-4",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
        ],
        [
          {
            top:true,
            right:false,
            bottom:true,
            left:false,
            title:"",
            author:"",
            date:""
          },
          {
            top:true,
            right:false,
            bottom:true,
            left:false,
            title:"",
            author:"",
            date:""
          },
          {
            top:true,
            right:true,
            bottom:false,
            left:false,
            title:"教材2-3",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
          {
            top:false,
            right:true,
            bottom:false,
            left:true,
            title:"教材2-4",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
        ],
        [
          {
            top:true,
            right:false,
            bottom:true,
            left:false,
            title:"",
            author:"",
            date:""
          },
          {
            top:true,
            right:true,
            bottom:false,
            left:false,
            title:"教材3-2",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
          {
            top:false,
            right:true,
            bottom:false,
            left:true,
            title:"教材3-3",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
        ],
        [
          {
            top:true,
            right:true,
            bottom:false,
            left:false,
            title:"教材4-1",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
          {
            top:false,
            right:true,
            bottom:false,
            left:true,
            title:"教材4-2",
            author:"Tatsuya Okazaki",
            date:"1ヶ月前"
          },
        ]
      ]
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
.materials_description_container{
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .materials_main_description{
    width: 90%;
    height: auto;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    .materials_main_description_image{
      background-color: chartreuse;
      width: 350px;
      height: 210px;
      margin: 20px;
      box-shadow: #00000033 2px 3px 6px;
    }
    .materials_main_description_text{
      width: calc(100% - 400px);
      height: 210px;
      margin: 20px;
      display: flex;
      flex-direction: column;
      .materials_main_description_text_title{
        width: 100%;
        font-size: 20px;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: flex-start;
      }
      .materials_main_description_text_tags_container{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .star_tag{
          border-radius: 4px;
          border: 1px solid #707070;
          display: flex;
          align-items: flex-end;
          justify-content: center;
          padding: 1px 5px;
          font-size: 12px;
          font-weight: 500;
        }
        .material_tag{
          background-color: #8FB0FF;
          border-radius: 4px;
          display: flex;
          align-items: flex-end;
          justify-content: center;
          padding: 2px 6px;
          margin: 5px 5px;
          font-size: 12px;
          font-weight: 500;
          color: #FEFEFE;
        }
      }
      .materials_main_description_text_date{
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        font-size: 13px;
        font-weight: 500;
      }
      .materials_main_description_text_description{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        font-size: 15px;
        font-weight: 500;
        margin: 2px 0px;
        p{
          width: 100%;
          text-align: left;
          display: flex;
          align-items: flex-start;
          justify-content: flex-start;
        }
      }
      .materials_main_description_text_author{
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .author{
          margin-right: 5px;
          font-size: 15px;
          font-weight: 500;
        }
        .follow_btn{
          padding: 5px 5px;
          border-radius: 4px;
          border: 1px solid #707070;
          margin-left: 20px;
          font-size: 13px;
          font-weight: 500;
        }
      }
    }
  }
  .materials_slide_description_container{
    width: 90%;
    height: 200px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    overflow-x: scroll;
    .slide{
      flex-shrink: 0;
      background-color: darkorange;
      width: 300px;
      height: 170px;
      margin: 10px;
      box-shadow: #00000033 2px 3px 6px;
    }
  }
  .btn_container{
    width: 90%;
    height: 60px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    .base_btn_style{
      cursor: pointer;
      padding: 5px 15px;
      margin: 10px;
      border: 1px solid #707070;
      border-radius: 5px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      color: #757474;
      font-size: 15px;
      font-weight: 600;
      transition: 0.2s;
    }
    .keep_btn{
      background-color: #FFFFFF;
      &:hover{
        color: #c09521;
      }
    }
    .dl_btn{
      background-color: #FFFFFF;
      &:hover{
        color: #5b856b;
      }
    }
    .comment_btn{
      background-color: #FFFFFF;
      &:hover{
        color: #6f70e7;
      }
    }
  }
  .comments_content_container{
    width: 90%;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    .comment_label_container{
      width: 100%;
      margin: 10px 0;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-start;
      .comment_label{
        margin-right: 10px;
        font-size: 25px;
        font-weight: 600;
        color: #242424;
      }
      .comment_number{
        font-size: 20px;
        font-weight: 500;
        color: #757474;
      }
    }
    .comments_container{
      width: 100%;
      height: auto;
      max-height: 500px;
      overflow-y: scroll;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      .comment_container{
        width: 90%;
        padding: 15px 0;
        border-top: 1px solid #E7E7E7;
        border-bottom: 1px solid #E7E7E7;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        .author_container{
          width: 100%;
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .author_image{
            background-color: crimson;
            width: 40px;
            height: 40px;
            border-radius: 50%;
          }
          .name_date_container{
            margin-left: 10px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: flex-start;
            .name{
              font-size: 15px;
              font-weight: 500;
              color: #242424;
            }
            .date{
              font-size: 13px;
              font-weight: 500;
              color: #757474;
            }
          }
        }
        .comments_description{
          width: 100%;
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: flex-start;
          p{
            width: 100%;
            text-align: left;
            display: flex;
            align-items: flex-start;
            justify-content: flex-start;
          }
        }
      }
    }
  }
  .branch_container{
    width: 100%;
    height: 550px;
    margin: 20px 0;
    background-image: url("../assets/bgs/bg_branch.png");
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    .branch_label_container{
      width: 70%;
      margin-top: 20px;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      .branch_label{
        width: 100%;
        padding: 5px;
        border-bottom: 2px solid #242424;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        .label{
          margin-right: 25px;
          font-size: 20px;
          font-weight: 600;
        }
        .update_number{
          font-size: 15px;
          font-weight: 500;
          color: #757474;
        }
      }
      .material_title{
        width: 100%;
        margin: 10px 0;
        font-size: 20px;
        font-weight: 500;
        display: flex;
        align-items: center;
        justify-content: flex-start;
      }
      .now_watchng{
        width: 100%;
        font-size: 15px;
        font-weight: 500;
        color: #42ABF2;
        display: flex;
        align-items: center;
        justify-content: flex-start;
      }
    }
    .branch_tree_container{
      background-color: #EEEEEE77;
      width: 70%;
      height: 400px;
      margin-bottom: 20px;
      overflow: scroll;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      .own_material{
        flex-shrink: 0;
        width: 250px;
        height: 155px;
        margin: 10px 0 0 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        .own_material_image{
          position: absolute;
          background-color: orange;
          width: 230px;
          height: 140px;
          left: 0;
          top: 0;
          box-shadow: #00000033 2px 3px 6px;
        }
        .own_material_title{
          position: absolute;
          width: auto;
          height: 50px;
          right: 0;
          bottom: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          .left_top{
            position: absolute;
            top: 0;
            left: 0;
            width: 15px;
            height: 15px;
            border-top: 2px solid #083D61;
            border-left: 2px solid #083D61;
          }
          .right_top{
            position: absolute;
            top: 0;
            right: 0;
            width: 15px;
            height: 15px;
            border-top: 2px solid #083D61;
            border-right: 2px solid #083D61;
          }
          .right_bottom{
            position: absolute;
            bottom: 0;
            right: 0;
            width: 15px;
            height: 15px;
            border-bottom: 2px solid #083D61;
            border-right: 2px solid #083D61;
          }
          .left_bottom{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 15px;
            height: 15px;
            border-bottom: 2px solid #083D61;
            border-left: 2px solid #083D61;
          }
          p{
            margin: 5;
            padding: 3px 20px;
            margin: 0 10px;
            background: transparent linear-gradient(103deg, #083D61 0%, #0F5787 45%, #105A8D 97%, #00416E 100%) 0% 0% no-repeat padding-box;
            box-shadow: 1px 1px 2px #00000029;
            border-radius: 3px;
            font-size: 20px;
            font-weight: 600;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
          }
        }
      }
      .branch_materials_cotainer{
        flex-shrink: 0;
        margin-top: 70px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        .branch_materials_row_cotainer{
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: flex-start;
          .branch_materials_container{
            margin-right: 10px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            .branch_border_container{
              width: 150px;
              height: 140px;
              margin: 0 10px;
              display: flex;
              align-items: center;
              justify-content: center;
              position: relative;
              .top{
                position: absolute;
                width: 4px;
                height: 72px;
                background-color: #333333;
                top: 0;
              }
              .right{
                position: absolute;
                width: 77px;
                height: 4px;
                background-color: #333333;
                right: 0;
              }
              .bottom{
                position: absolute;
                width: 4px;
                height: 72px;
                background-color: #333333;
                bottom: 0;
              }
              .left{
                position: absolute;
                width: 77px;
                height: 4px;
                background-color: #333333;
                left: 0;
              }
            }
            .branch_material_title{
              position: relative;
              width: 250px;
              height: 50px;
              display: flex;
              align-items: center;
              justify-content: center;
              .left_top{
                position: absolute;
                top: 0;
                left: 0;
                width: 15px;
                height: 15px;
                border-top: 2px solid #083D61;
                border-left: 2px solid #083D61;
              }
              .right_top{
                position: absolute;
                top: 0;
                right: 0;
                width: 15px;
                height: 15px;
                border-top: 2px solid #083D61;
                border-right: 2px solid #083D61;
              }
              .right_bottom{
                position: absolute;
                bottom: 0;
                right: 0;
                width: 15px;
                height: 15px;
                border-bottom: 2px solid #083D61;
                border-right: 2px solid #083D61;
              }
              .left_bottom{
                position: absolute;
                bottom: 0;
                left: 0;
                width: 15px;
                height: 15px;
                border-bottom: 2px solid #083D61;
                border-left: 2px solid #083D61;
              }
              p{
                width: 240px;
                height: 35px;
                margin: 5;
                padding: 3px 20px;
                margin: 0 10px;
                background: transparent linear-gradient(103deg, #083D61 0%, #0F5787 45%, #105A8D 97%, #00416E 100%) 0% 0% no-repeat padding-box;
                box-shadow: 1px 1px 2px #00000029;
                border-radius: 3px;
                font-size: 15px;
                font-weight: 600;
                color: #FFFFFF;
                display: flex;
                align-items: center;
                justify-content: center;
              }
              .branch_material_author{
                position: absolute;
                top: -45px;
                width: 250px;
                height: 40px;
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: center;
                .author_image{
                  width: 40px;
                  height: 40px;
                  border-radius: 99px;
                  background-color: crimson;
                  margin-right: 10px;
                }
                .author_date_container{
                  display: flex;
                  flex-direction: column;
                  align-items: flex-start;
                  justify-content: center;
                  color: #757474;
                  font-size: 15px;
                  font-weight: 600;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>