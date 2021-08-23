import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data:{
        "model": "",
        "pk": Number,
        "fields": {
            "username": "",
            "password": "",
            "email": "",
            "isdonor": "非捐赠者",
            "create_time": "",
            "money": 0,
        } ,
        username:'账号失效，请重新登录',
        isdonor:'非捐赠者',
        email:'账号失效，请重新登录',
        create_time:'账号失效，请重新登录',
        money:0,
        seen1:true,
        seen2:false,
        isdisabled:true,
        nowtime:'',
        isattribute:'未知',
    },
  },
  mutations: {
    GetUserInfo(state, userinfo){
      state.data = userinfo; //获取后端用户数据
      state.data.username  = state.data[0].fields.username; //保存usernam数据
      state.data.email  = state.data[0].fields.email;
      state.data.isdonor  = state.data[0].fields.isdonor; //保存捐赠者数据
      state.data.create_time  = state.data[0].fields.create_time; //保存用户创建时间数据
      state.data.nowtime = new Date(); //获取当前时间
      //判断用户属性
      if (state.data.nowtime.getMonth()+1 == Number(state.data.create_time.charAt(5)+state.data.create_time.charAt(6)))
      {
        state.data.isattribute = '初出茅庐';
      }
      else
      {
        state.data.isattribute = '略知一二';
        console.log(state.data.isattribute);
      }
      state.data.money  = state.data[0].fields.money; //保存金币数据
      state.data.seen1 = false; //设置头像数据
      state.data.seen2 = true; //设置头像数据
      state.data.isdisabled = false; //设置账号导航是否可点击
    },
    
  },
  actions: {
  },
  modules: {
  }
})
