// import axios from 'axios'
// import { useEffect, useState } from 'react'


// const CollectData =(url) => {
//     const [fetch, setFetching] = useState({isFetching:false})
//     const [dataState, setDataState] = useState({data: []})


//     useEffect(()=> {
//         const fetchDataFromApi = async () => {
//             try{
//                 setFetching({isFetching:true})
//                 const response = await axios.get('')
//                 console.log(response.data)
//                 setDataState({...dataState, data: response.data})
//             }catch(err){
//                 setFetching({...fetch, isFetching:true})
//                 console.log(err)
//             }
//         }
//         fetchDataFromApi()
//     }, []);
// return (
//     [dataState]
// )
// }

// export default CollectData;
    

import { useEffect, useState } from 'react';
import axios from 'axios';

const useCollectData = (url) => {
    const [dataState, setDataState] = useState([]);

    const fetchDataFromApi = async () => {
        try{
            const response = await axios.get(url)
            setDataState(response.data);
        } catch (err) {
            console.log(err)
        }
    };

    useEffect(() => {
        fetchDataFromApi();
    }, []);

    return (
        [dataState]
    )

};

export default useCollectData