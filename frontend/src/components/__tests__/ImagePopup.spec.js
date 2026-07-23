import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import ImagePopup from '../ImagePopup.vue';

describe('ImagePopup.vue', () => {
  const sampleWaypoint = {
    id: 1,
    title: 'Bivouac Kvalvika',
    description: 'Beautiful beach bivouac',
    lat: 68.0442,
    lng: 13.0931,
    image_path: '/api/images/sample.jpg'
  };

  it('renders waypoint details when provided', () => {
    const wrapper = mount(ImagePopup, {
      props: { waypoint: sampleWaypoint }
    });

    expect(wrapper.text()).toContain('Bivouac Kvalvika');
    expect(wrapper.text()).toContain('Beautiful beach bivouac');
    expect(wrapper.find('img').attributes('src')).toBe('/api/images/sample.jpg');
  });

  it('emits close event when close button is clicked', async () => {
    const wrapper = mount(ImagePopup, {
      props: { waypoint: sampleWaypoint }
    });

    await wrapper.find('.close-btn').trigger('click');
    expect(wrapper.emitted('close')).toBeTruthy();
  });
});
