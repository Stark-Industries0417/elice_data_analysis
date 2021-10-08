import './firstChoice.scss';
import React from 'react';
import { Link } from 'react-router-dom';
import Marginer from '../../components/marginer';
import TastesCategory from '../../const/tastesCategory';

export default function FirstChoice() {
  return (
    <div className="CategoryContainer">
      <Marginer direction="vertical" margin="2rem" />
      <h1>카테고리를 선택하세요</h1>
      <Marginer direction="vertical" margin="2rem" />
      <div className="choiceContainer">
        {TastesCategory.map(tastes => (
          <Link to={`/what-to-eat/category/${tastes}`}>
            <button type="button" className="menuCategory">
              <img alt="" className="CategoryImage" /> {tastes}
            </button>
          </Link>
        ))}
      </div>

      <div className="buttonContainer">
        <Link to="/what-to-eat/">
          <button type="button" className="button-prev">
            이전
          </button>
        </Link>
      </div>
    </div>
  );
}
