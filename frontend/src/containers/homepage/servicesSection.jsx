import React from "react";
import { Element } from "react-scroll";
import styled from "styled-components";
import { Marginer } from "../../components/marginer";
import { SectionTitle } from "../../components/sectionTitle";
import { TabComponent } from "../../components/tabs";

const ServicesContainer = styled(Element)`
  width: 100%;
  min-height: 900px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 10px;
`;

export function ServicesSection(props) {
  return (
    <ServicesContainer name="servicesSection">
      <Marginer direction="vertical" margin="2em" />
      <SectionTitle>리뷰왕이 제공하는 서비스입니다.</SectionTitle>
      <Marginer direction="vertical" margin="3em" />
      <TabComponent/>
    </ServicesContainer>
  );
}
