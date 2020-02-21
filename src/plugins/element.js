import Vue from 'vue'
import { Button, Form, FormItem, Input, Alert, Message, Container, Header, Aside, Main } from 'element-ui'

Vue.use(Button)
Vue.use(Form).use(FormItem)
Vue.use(Input)
Vue.use(Alert)
Vue.use(Container).use(Header).use(Aside).use(Main)
Vue.prototype.$message = Message
