$(function () {
  $('.bxslider').bxSlider({
    mode: 'horizontal',
    captions: false,
    slideWidth: 5220, // tamaño de slider
    auto: true, // para que sea automatico
    keyboardEnabled: true, // para que puedas cambiar con
    speed: 500,
    pause: 10000,
  });
});

Vue.config.devtools = true;

Vue.component('card', {
  template: `
    <div class="card-wrap"
      @mousemove="handleMouseMove"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
      ref="card">
      <div class="card"
        :style="cardStyle">
        <div class="card-bg" :style="[cardBgTransform, cardBgImage]"></div>
        <div class="card-info">
          <slot name="header"></slot>
          <slot name="content"></slot>
        </div>
      </div>
    </div>`,
  mounted() {
    this.width = this.$refs.card.offsetWidth;
    this.height = this.$refs.card.offsetHeight;
  },
  props: ['dataImage'],
  data: () => ({
    width: 0,
    height: 0,
    mouseX: 0,
    mouseY: 0,
    mouseLeaveDelay: null
  }),

  computed: {
    mousePX() {
      return this.mouseX / this.width;
    },
    mousePY() {
      return this.mouseY / this.height;
    },
    cardStyle() {
      const rX = this.mousePX * 30;
      const rY = this.mousePY * -30;
      return {
        transform: `rotateY(${rX}deg) rotateX(${rY}deg)`
      };

    },
    cardBgTransform() {
      const tX = this.mousePX * -40;
      const tY = this.mousePY * -40;
      return {
        transform: `translateX(${tX}px) translateY(${tY}px)`
      };

    },
    cardBgImage() {
      return {
        backgroundImage: `url(${this.dataImage})`
      };

    }
  },

  methods: {
    handleMouseMove(e) {
      this.mouseX = e.pageX - this.$refs.card.offsetLeft - this.width / 2;
      this.mouseY = e.pageY - this.$refs.card.offsetTop - this.height / 2;
    },
    handleMouseEnter() {
      clearTimeout(this.mouseLeaveDelay);
    },
    handleMouseLeave() {
      this.mouseLeaveDelay = setTimeout(() => {
        this.mouseX = 0;
        this.mouseY = 0;
      }, 1000);
    }
  }
});

const app = new Vue({
  el: '#app'
});

const slideWidth = 30;

const _items = [
  {
    player: {
      title: 'Camuflaje Militar',
      image: 'https://ik.imagekit.io/Bc/carrusel3.webp'
    }
  },


  {
    player: {
      title: "Miles Morales - Hombre araña",
      image: 'https://ik.imagekit.io/Bc/carrusel4.webp'
    }
  },


  {
    player: {
      title: 'Monstruo de Frankenstein',
      image: 'https://ik.imagekit.io/Bc/carrusel5.webp'
    }
  },


  {
    player: {
      title: 'Aprendiz de Bruja',
      image: 'https://ik.imagekit.io/Bc/carrusel6.webp'
    }
  },


  {
    player: {
      title: 'Espantapájaros',
      image: 'https://ik.imagekit.io/Bc/carrusel7.webp'
    },
  }];


const length = _items.length;
_items.push(..._items);

const sleep = (ms = 0) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

const createItem = (position, idx) => {
  const item = {
    styles: {
      transform: `translateX(${position * slideWidth}rem)`
    },

    player: _items[idx].player
  };

  switch (position) {
    case length - 1:
    case length + 1:
      item.styles = { ...item.styles, filter: 'grayscale(1)' };
      break;
    case length:
      break;
    default:
      item.styles = { ...item.styles, opacity: 0 };
      break;
  }

  return item;
};

const CarouselSlideItem = ({ pos, idx, activeIdx }) => {
  const item = createItem(pos, idx, activeIdx);

  return /*#__PURE__*/(
    React.createElement("li", { className: "carousel__slide-item", style: item.styles }, /*#__PURE__*/
      React.createElement("div", { className: "carousel__slide-item-img-link" }, /*#__PURE__*/
        React.createElement("img", { src: item.player.image, alt: item.player.title })), /*#__PURE__*/

      React.createElement("div", { className: "carousel-slide-item__body" }, /*#__PURE__*/
        React.createElement("h4", null, item.player.title), /*#__PURE__*/
        React.createElement("p", null, item.player.desc))));

};

const keys = Array.from(Array(_items.length).keys());

const Carousel = () => {
  const [items, setItems] = React.useState(keys);
  const [isTicking, setIsTicking] = React.useState(false);
  const [activeIdx, setActiveIdx] = React.useState(0);
  const bigLength = items.length;

  const prevClick = (jump = 1) => {
    if (!isTicking) {
      setIsTicking(true);
      setItems(prev => {
        return prev.map((_, i) => prev[(i + jump) % bigLength]);
      });
    }
  };

  const nextClick = (jump = 1) => {
    if (!isTicking) {
      setIsTicking(true);
      setItems(prev => {
        return prev.map(
          (_, i) => prev[(i - jump + bigLength) % bigLength]);

      });
    }
  };

  const handleDotClick = idx => {
    if (idx < activeIdx) prevClick(activeIdx - idx);
    if (idx > activeIdx) nextClick(idx - activeIdx);
  };

  React.useEffect(() => {
    if (isTicking) sleep(300).then(() => setIsTicking(false));
  }, [isTicking]);

  React.useEffect(() => {
    setActiveIdx((length - items[0] % length) % length); // prettier-ignore
  }, [items]);

  return /*#__PURE__*/(
    React.createElement("div", { className: "carousel__wrap" }, /*#__PURE__*/
      React.createElement("div", { className: "carousel__inner" }, /*#__PURE__*/
        React.createElement("button", { className: "carousel__btn carousel__btn--prev", onClick: () => prevClick() }, /*#__PURE__*/
          React.createElement("i", { className: "carousel__btn-arrow carousel__btn-arrow--left" })), /*#__PURE__*/

        React.createElement("div", { className: "carousel__container" }, /*#__PURE__*/
          React.createElement("ul", { className: "carousel__slide-list" },
            items.map((pos, i) => /*#__PURE__*/
              React.createElement(CarouselSlideItem, {
                key: i,
                idx: i,
                pos: pos,
                activeIdx: activeIdx
              })))), /*#__PURE__*/

        React.createElement("button", { className: "carousel__btn carousel__btn--next", onClick: () => nextClick() }, /*#__PURE__*/
          React.createElement("i", { className: "carousel__btn-arrow carousel__btn-arrow--right" })), /*#__PURE__*/

        React.createElement("div", { className: "carousel__dots" },
          items.slice(0, length).map((pos, i) => /*#__PURE__*/
            React.createElement("button", {
              key: i,
              onClick: () => handleDotClick(i),
              className: i === activeIdx ? 'dot active' : 'dot'
            }))))));

};

ReactDOM.render( /*#__PURE__*/React.createElement(Carousel, null), document.getElementById('root'));
