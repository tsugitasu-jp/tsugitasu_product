hoge.vue

<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.2.2/jszip.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>

<template>
  <div id="search-ip">
    <div>
      <form id="upload_form" enctype="multipart/form-data">
          <input @change="selectedFile" type="file" name="file">
          <input @change="selectedMainImage" type="file" name="file" accept="image/*">
          <input @change="selectedSubImage" type="file" name="file" accept="image/*">
          <button @click="upload" type="button">アップロード</button>
      </form>
    </div>
  </div>
</template>


<script>
  function array_to_formdata(data, formData){
    Object.keys(data).forEach(key => {
      const value = data[key];
      if (Array.isArray(value)) {
        value.forEach(entry => {
          formData.append(key + '[]', entry);
        });
      } else {
        formData.append(key, value);
      }
    });
  }
  
  export default {
    name: 'SearchIp',
    methods: {
      selectedFile(e) {
        // 選択された File の情報を保存しておく
        e.preventDefault();
        let files = e.target.files;
        this.uploadFile = files[0];
      },

      selectedMainImage(e) {
        // 選択された File の情報を保存しておく
        e.preventDefault();
        let files = e.target.files;
        this.image_main = files[0];
      },

      selectedSubImage(e) {
        // 選択された File の情報を保存しておく
        e.preventDefault();
        let files = e.target.files;
        this.image_subs = {"image_sub": [files[0], files[0]]};
      },

      upload() {
        // FormData を利用して File等 を POST する
        let formData = new FormData();
        formData.append('fd', this.uploadFile);
        formData.append('image_main', this.image_main)
        formData.append('title', "算数の良問集")
        formData.append('context', "小学校三年生の算数の良問を集めました。ぜひご活用ください")
        formData.append('tag_flag', true)

        array_to_formdata(this.image_subs, formData)
        array_to_formdata({'tag': ["算数", "三年生"]}, formData)

        let config = {
          headers: {
            'content-type': 'multipart/form-data'
          },
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
    }
  }

</script>