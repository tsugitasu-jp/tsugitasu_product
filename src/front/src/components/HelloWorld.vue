hoge.vue

<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.2.2/jszip.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>

<template>
  <div id="search-ip">
    <div>
      <div>
        <input @click="getFile" type="button" value="ファイルを取得">
      </div>
      <form id="upload_form" enctype="multipart/form-data">
          <input @change="selectedFile" type="file" name="file">
          <button @click="upload" type="button">アップロード</button>
      </form>
    </div>
  </div>
</template>


<script>

  var AWS = require('aws-sdk');
  AWS.config.update(
    {
      accessKeyId: "AKIAQ7J3FIK6FGBSTY7Q",
      secretAccessKey: "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",
    }
  );
  var s3 = new AWS.S3();

  const bucket_name = "tsugitasu-static"
 

  export default {
    name: 'SearchIp',
    methods: {
      selectedFile(e) {
        // 選択された File の情報を保存しておく
        e.preventDefault();
        let files = e.target.files;
        this.uploadFile = files[0];
      },

      upload() {
        // FormData を利用して File を POST する
        let formData = new FormData();
        formData.append('fd', this.uploadFile);
        let config = {
          headers: {
            'content-type': 'multipart/form-data'
          },
          body: {
            "file_name": "favicon.ico",
            "content_image_main":  "math_image.jpg",
            "content_image_subs": ["math_image1.jpg", "math_image.3png"],
            "title": "算数の良問集",
            "context": "小学校三年生の算数の良問を集めました。ぜひご活用ください",
            "tag": ["算数", "三年生"],
            "tag_flag": true
          }
        };
        this.axios
          .post('http://127.0.0.1:8000/api-v1/content/create/', formData, config)
          .then(function(response) {
              console.log("OK!")
          })
          .catch(function(error) {
              // error 処理
          })
      },
      
      getFile() {
        s3.getObject(
          { 
            Bucket: bucket_name, 
            Key: "media/images/login_pic.2ee7e652.png" 
          },
          function (error, data) {
            if (error != null) {
              alert("Failed to retrieve an object: " + error);
            } else {
              const blob = new Blob([data.Body], {type: data.ContentType});
              var zip = new JSZip();
              zip.file("login_pic.2ee7e652.png", blob);
              //zip.file("login_pic.png", blob);
              zip.generateAsync({type:"blob"})
                 .then(function(content) {
                    saveAs(content, "example.zip");
                 });

              //const fileURL = window.URL.createObjectURL(blob);
              //const link = document.createElement('a')
              //link.href = fileURL
              //link.download = "login_pic.2ee7e652.png"
              //link.click()
              //document.body.removeChild(link);
            }
          }
        );
      }
    }
  }
</script>