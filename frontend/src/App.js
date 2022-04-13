import React from 'react';
import axios from 'axios';
// import logo from './logo.svg';
import './App.css';
import MainMenu from './components/MainMenu.js';
//import UserList from './components/User.js';
import AuthorList from "./components/Author";
import Footer from './components/Footer.js';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'authors': []
        }
    }
    componentDidMount() {

       // const authors = [
       //     {
       //        'first_name': 'Фёдор',
       //        'last_name': 'Достоевский',
       //        'birthday_year': 1821
       //     },
       //     {
       //        'first_name': 'Пушкин',
       //        'last_name': 'Александр',
       //        'birthday_year': 1820
       //     },
       //     ]
       // this.setState({
       //                'authors': authors
       //             })
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                this.setState(
                            {
                               'authors': authors
                            }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <MainMenu />
                {/*<UserList users={this.state.users} />*/}
                <AuthorList authors={this.state.authors} />
                <Footer />
            </div>
        )
    }
}

export default App;