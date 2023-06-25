import { useState , useEffect } from "react"
export const useUser=(test)=>{
	const [user,setUser] = useState({})
	const [users,setUsers]=useState([])
   	useEffect(()=>{
   		if (test) {
   			setUser({user_name:"admin",email:"admin@admin.con",followers:[],followed:[],posts:[]})
   			setUsers([{user_name:"test",email:"test@test.con",followers:[],followed:[],posts:[]}])
   		}
		let user_id=parseInt(document.cookie.match(/\d$/g)[0])
		fetch(`/api/users/${user_id}`)
		.then(response=>response.json())
		.then(json=>{console.log(json); setUser(json)})
      	fetch('/api/users').then(response=>response.json())
      	.then(json =>{console.log(json);setUsers(json)})
   	},[])
	return {user,users}
}

export const usePosts=()=>{
	const [posts,setPosts] = useState([])
	useEffect(()=>{fetch("/api/posts").then(r=>r.json()).then(j=>setPosts(j))},[])
	return {posts}
}