import './rankContent.scss';
import { Link } from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Marginer from '../../components/marginer';
import MenuCategory from '../../const/menuCategory';

export default function RankContent() {
  const [tests, setTests] = useState();

  // API로 부터 카테고리 정보 & 이미지를 받아옴(id: 36~70)
  const GetCategoryAPI = async () => {
    const CategoryResponse = await axios.get(`http://3.139.100.234:5000/ranks`);
    setTests(CategoryResponse.data);
    console.log('CategoryResponse', CategoryResponse.data);
    return CategoryResponse.data;
  };

  useEffect(() => {
    GetCategoryAPI();
  }, []);

  console.log(tests);

  return (
    <div className="RankContainer">
      <Marginer direction="vertical" margin="3rem" />
      <h2 className="TitleText"> 업종별 순위 예시</h2>
      <Marginer direction="vertical" margin="4rem" />

      <div className="choiceRankContainer">
        {MenuCategory.data.map(option => (
          <Link to={`/rank/result/${option.category_id}`}>
            <button type="button" className="menuCategory">
              {option.category}
            </button>
          </Link>
        ))}
      </div>

      <Marginer direction="vertical" margin="8rem" />
    </div>
  );
}
