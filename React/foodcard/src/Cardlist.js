// import React from 'react';
// import { Image } from 'react-native';

const Cardlist = ({ cards }) => {
    // const cards = props.cards;
    console.log(cards) //?? why object here
    return ( 
        <div className="card-list">
            {cards.cards.map((card)=>(
                <div className="card-preview" key={card.id}>
                    <h2>{ card.title }</h2>
                    {/* <Image source={ card.body } /> */}
                    {/* <Image style={styles.center} source={require('./assets/cat1.jpg')} /> */}
                    <img src={ card.body } alt="Cover" />
                    <p>{ card.stars }</p>
                </div>
            ))}
        </div>
    );
}

export default Cardlist;