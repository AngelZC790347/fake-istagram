import { useEffect, useState } from 'react'
import {useUser}  from './services/userService'
import { Link,Routes,Route,createBrowserRouter} from 'react-router-dom'
import buscadorLogo from '/buscador.svg'
import istagramTittle from '/istagram.svg'
import reelsLogo from '/reels.svg'
import notificationLogo from '/notification.svg'
import configLogo from '/config.svg'
import avatarLogo from '/avatar.svg'
import newPostLogo from '/newPost.svg'
import inicioLogo from '/inicio.svg'
import explorationLogo from '/exploration.svg'
import chatLogo from '/chat.svg'
import Incio from './Incio.jsx'
import Profile from './pages/Profile.jsx'
import PageNotFound from './pages/error-page.jsx'
import './App.css'
function App() {
   const {user,users} = useUser(false)
   const router = [
      {
         path: "",
         element: <Incio/>,
         logo:inicioLogo
      },
      {
         path: "buscar",
         element: <input type="search" placeholder="Buscar .../t🔎"/>,
         logo:buscadorLogo
      },
      {
         path: "explorar",
         element: <h1>explorar</h1>,
         logo:explorationLogo
      },
      {
         path: "reels",
         element: <h1>reels</h1>,
         logo:reelsLogo
      },
      {
         path: "mensajes",
         element: <h1>mensajes</h1>,
         logo:chatLogo
      },
      {
         path: "notificaciones",
         element: <h1>notificaciones</h1>,
         logo:notificationLogo
      },
      {
         path: "crear",
         element: <a href="./posts">Post Page</a>,
         logo:newPostLogo
      },
      {
         path: user.user_name,
         element: <Profile usuario={user}></Profile>,
         logo:avatarLogo
      },
   ];
   users.map(current_user=>{
      if(current_user.user_name != user.user_name) router.push({path:current_user.user_name,element:<Profile usuario={current_user}></Profile>,logo:avatarLogo})
   })
   return (
      <div className='container'>
         <nav>
            <img src={istagramTittle} alt="" height="15" />
            <ul>
               {router.map((el,index)=>index<=7?<li><Link to={el.path}><img src={el.logo} alt="" /><h2>{el.path==""?"inicio":el.path}</h2></Link></li>:null)}
            </ul>
         </nav>
         <div id='content'>
             <Routes>
               {router.map((el)=><Route path={el.path} element={el.element}/>)}
               <Route path='*' element={<PageNotFound/>}/>
              </Routes>             
         </div>
      </div>
   )
}

export default App
